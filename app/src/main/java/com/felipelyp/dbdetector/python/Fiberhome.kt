package com.felipelyp.dbdetector.python

import com.chaquo.python.PyObject

class Host(val value: String)
class Port(val value: Int)
class User(val value: String)
class Pass(val value: String)

class Fiberhome(private val olt: PyObject) : BaseConnect {

    override fun connect(host: Host, port: Port, user: User, pass: Pass) {
        olt.callAttr("connect", host.value, port.value, user.value, pass.value)
    }

    fun cdGponOnu() {
        olt.callAttr("cd_gpononu")
    }

    fun cdExit() {
        olt.callAttr("cd_exit")
    }

    fun cdQinq() {
        olt.callAttr("cd_qinq")
    }

    fun showOnlineOnu(slot: Int, pon: Int): String {
        val result = olt.callAttr("show_online_onu", slot, pon)
        return result.toString()
    }

    fun showOpticModule(slot: Int, pon: Int, onu: Int): String {
        val result = olt.callAttr("show_optic_module", slot, pon, onu)
        return result.toString()
    }
}