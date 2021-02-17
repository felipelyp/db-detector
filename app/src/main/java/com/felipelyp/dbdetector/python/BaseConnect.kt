package com.felipelyp.dbdetector.python

interface BaseConnect {
    fun connect(host: Host, port: Port, user: User, pass: Pass)
}