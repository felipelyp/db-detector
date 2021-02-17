package com.felipelyp.dbdetector.ui.home

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.felipelyp.dbdetector.R
import com.felipelyp.dbdetector.python.*
import kotlinx.coroutines.*
import org.koin.android.ext.android.inject

class HomeActivity : AppCompatActivity() {

    private val fiberhome: Fiberhome by inject()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)
        setSupportActionBar(findViewById(R.id.toolbar))

        GlobalScope.launch(Dispatchers.IO) {
            fiberhome.connect(
                Host("192.169.99.254"),
                Port(23),
                User("GEPON"),
                Pass("GEPON")
            )

            fiberhome.cdGponOnu()
            val result = fiberhome.showOnlineOnu(11, 1)

            withContext(Dispatchers.Main) {
                findViewById<TextView>(R.id.textView).text = result
            }
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_settings -> true
            else -> super.onOptionsItemSelected(item)
        }
    }
}