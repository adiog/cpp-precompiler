# -*- coding: utf-8 -*-

"""
This file is a part of quicksave project.
Copyright (c) 2016 Aleksander Gajewski <adiog@brainfuck.pl>,
                   Adam Morawski <poczta@adammorawski.pl>.
"""

REPLACE='''
#include <mutex>
#include <future>
#include <thread>

#define CO_YIELD(value) \
    isRunning = false; \
    promise.set_value(value); \
    cv.wait(unique_lock, [this](){return isTerminated || isRunning;}); \
    if (isTerminated) return;

#define CO_RETURN(value) \
    isRunning = false; \
    promise.set_value(value); \
    isReturned = true; \
    return;

class CoRutClass {
public:
    CoRutClass() = default;
    ~CoRutClass() {
        isTerminated = true;
        cv.notify_all();
        thr.join();
    }

    using ReturnType = ___COROUTINE_RETURN_TYPE___;

    void corut_thread(___COROUTINE_PARAMS___) {
        std::unique_lock <std::mutex> unique_lock(mutex);
        ___COROUTINE_BODY___
    }

    template<typename... Args>
    ReturnType start(Args... args) {
        if (isStarted) {
            throw std::runtime_error("");
        } else {
            isStarted = true;
            thr = std::thread{[&]() { this->corut_thread(args...); }};
            return resume();
        }
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

    bool isFinished() { return isReturned; }

private:
    std::thread thr;
    std::mutex mutex;
    std::condition_variable cv;
    std::promise <ReturnType> promise;
    bool isStarted = false;
    bool isRunning = false;
    bool isReturned = false;
    bool isTerminated = false;
} ___COROUTINE_NAME___;
'''



#//co_yield 666;
#CO_YIELD(666)
#
#
#for (int i = 0; i < 5; ++i) {
#//co_yield i * factor;
#CO_YIELD(i*factor)
#}

#//co_return 5;
#CO_RETURN(541)

