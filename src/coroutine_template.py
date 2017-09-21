# -*- coding: utf-8 -*-

"""
This file is a part of cpp-precompiler project.
Copyright (c) 2016 Aleksander Gajewski <adiog@brainfuck.pl>,
"""

COROUTINE_TEMPLATE = '''
#include <mutex>
#include <future>
#include <thread>

#include <tuple>

#ifndef COROUTINE_GENERATOR
#define COROUTINE_GENERATOR

namespace adg {

template <std::size_t... Is> auto index_over(std::index_sequence<Is...>) {
  return [](auto &&f) -> decltype(auto) {
    return decltype(f)(f)(std::integral_constant<std::size_t, Is>{}...);
  };
}
template <std::size_t N>
auto index_upto(std::integral_constant<std::size_t, N> = {}) {
  return index_over(std::make_index_sequence<N>{});
}

template <class F, class Tuple> decltype(auto) apply(F &&f, Tuple &&tup) {
  auto indexer =
      index_upto<std::tuple_size<std::remove_reference_t<Tuple>>::value>();
  return indexer([&](auto... Is) -> decltype(auto) {
    return std::forward<F>(f)(std::get<Is>(std::forward<Tuple>(tup))...);
  });
}
}

template <typename CoroutineClass, typename InvokeArgs> class Iterator {
public:
  Iterator(CoroutineClass &coroutine, InvokeArgs args)
      : coroutine(coroutine), args(args) {}

  typename CoroutineClass::ReturnType operator*() {
    if (!coroutine.isStarted()) {
      value = adg::apply(
          [&](auto... args) { return coroutine.invoke(args...); }, args);
    }
    return value;
  }

  void operator++() { value = coroutine.resume(); }

  bool operator!=(const Iterator &sentinel) { return !coroutine.isFinished(); }
  bool operator<(const Iterator &sentinel) { return !coroutine.isFinished(); }

private:
  typename CoroutineClass::ReturnType value;
  CoroutineClass &coroutine;
  InvokeArgs args;
};

template <typename CoroutineClass, typename TupledArgs> class Generator {
public:
  Generator(CoroutineClass &coroutine, TupledArgs &&args)
      : coroutine(coroutine), args(std::move(args)) {}
  Iterator<CoroutineClass, TupledArgs> begin() {
    coroutine.reset();
    return Iterator<CoroutineClass, TupledArgs>{coroutine, args};
  }
  Iterator<CoroutineClass, TupledArgs> end() {
    return Iterator<CoroutineClass, TupledArgs>{coroutine, args};
  }

private:
  CoroutineClass &coroutine;
  TupledArgs args;
};

template <typename CoroutineClass, typename... Args>
Generator<CoroutineClass, std::tuple<Args...>>
generator(CoroutineClass &coroutine, Args... args) {
  return Generator<CoroutineClass, std::tuple<Args...>>(
      coroutine, std::tuple<Args...>{args...});
}

#endif


thread_local class CoroutineClass____COROUTINE_NAME___ {
public:
    using ReturnType = ___COROUTINE_RETURN_TYPE___;

    CoroutineClass____COROUTINE_NAME___() = default;
    ~CoroutineClass____COROUTINE_NAME___() {
        finalize();
    }

    void reset() {
        if (isStartedFlag) {
            finalize();
            initialize();
        }
    }

    void initialize() {
        isStartedFlag = false;
        isRunning = false;
        isReturned = false;
        isTerminated = false;
    }

    void finalize() {
        {
            std::unique_lock<std::mutex> unique_lock(mutex);
            isTerminated = true;
        }
        cv.notify_all();
        if (thr.joinable()) {
            thr.join();
        }
    }

    void corut_thread(___COROUTINE_PARAMS___) {
        std::unique_lock <std::mutex> unique_lock(mutex);
        ___COROUTINE_BODY___
    }

    template<typename... Args>
    ReturnType invoke(Args... args) {
        if (isStartedFlag) {
            reset();
        }
        
        isStartedFlag = true;
        thr = std::thread{[&]() { this->corut_thread(args...); }};
        return resume();
    }
    
    template<typename... Args>
    ReturnType operator()(Args... args) {
        return invoke(args...);
    }

    ReturnType resume() {
        ReturnType return_value = promise.get_future().get();
        {
            std::unique_lock<std::mutex> unique_lock(mutex);
            promise = std::promise<ReturnType>{};
            isRunning = true;
        }
        cv.notify_one();
        return return_value;
    }

    bool isStarted() { return isStartedFlag; }
    bool isFinished() { return isReturned; }

private:
    std::thread thr;
    std::mutex mutex;
    std::condition_variable cv;
    std::promise <ReturnType> promise;
    bool isStartedFlag = false;
    bool isRunning = false;
    bool isReturned = false;
    bool isTerminated = false;
} ___COROUTINE_NAME___;
'''
