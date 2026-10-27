import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
BOT_TOKEN="9118559285:AAGx1KnCDTu7dpPeSJ7m9sm9zipeRVe_GKU"
API_KEY="bc410a2f66f981790823ef2964d5ec43"
API_URL="https://smmcpan.com/api/v2"
def api_call(d):
 d['key']=API_KEY
 return requests.post(API_URL,data=d,timeout=20).json()
async def start(update,context):
 kb=[[InlineKeyboardButton("🛒 الخدمات",callback_data="services")],[InlineKeyboardButton("💳 رصيدي",callback_data="balance")]]
 await update.message.reply_text(f"بوت طلباتي شغال ✅\nايدك: {update.effective_user.id}",reply_markup=InlineKeyboardMarkup(kb))
async def btn(update,context):
 q=update.callback_query;await q.answer()
 if q.data=="services":
  r=api_call({"action":"services"});txt="\n".join([f"{x['service']} - {x['name'][:30]}" for x in r[:20]]);await q.message.reply_text(txt[:4000])
 else:
  r=api_call({"action":"balance"});await q.message.reply_text(str(r))
app=Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CallbackQueryHandler(btn))
app.run_polling()
