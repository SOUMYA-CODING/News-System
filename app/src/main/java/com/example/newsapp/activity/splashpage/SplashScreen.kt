package com.example.newsapp.activity.splashpage

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import com.example.newsapp.R
import com.example.newsapp.activity.homepage.HomeScreen
import com.example.newsapp.activity.language.LanguageSelectionScreen

@SuppressLint("CustomSplashScreen")
class SplashScreen : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash_screen)

        // Variable Declaration
        val splashScreenTime: Long = 1000

        Handler(Looper.getMainLooper()).postDelayed({
            val intent = Intent(this, HomeScreen::class.java)
            startActivity(intent)
            finish()
        }, splashScreenTime)
    }
}