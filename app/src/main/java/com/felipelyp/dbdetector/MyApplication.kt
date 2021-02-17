@file:Suppress("unused")

package com.felipelyp.dbdetector

import android.app.Application
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import com.felipelyp.dbdetector.koin.appModule
import org.koin.android.ext.koin.androidContext
import org.koin.core.context.startKoin

class MyApplication : Application() {

    override fun onCreate() {
        super.onCreate()

        startKoin {
            androidContext(this@MyApplication)
            modules(appModule)
        }

        if(!Python.isStarted()) {
            Python.start(AndroidPlatform(this))
        }
    }
}