package com.felipelyp.dbdetector.koin

import com.chaquo.python.Python
import com.felipelyp.dbdetector.python.Fiberhome
import org.koin.dsl.module

val appModule = module {
    //Chaquopy
    single { Python.getInstance() }

    //Fiberhome
    single { Fiberhome(get<Python>().getModule("fiberhome")) }
}