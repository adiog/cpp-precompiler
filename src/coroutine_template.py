# -*- coding: utf-8 -*-

"""
This file is a part of cpp-precompiler project.
Copyright (c) 2016 Aleksander Gajewski <adiog@brainfuck.pl>,
"""

COROUTINE_TEMPLATE = '''
#include <mutex>
#include <future>
#include <thread>

class CoroutineClass____COROUTINE_NAME___ {
public:
    CoroutineClass____COROUTINE_NAME___() = default;
    ~CoroutineClass____COROUTINE_NAME___() {
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
