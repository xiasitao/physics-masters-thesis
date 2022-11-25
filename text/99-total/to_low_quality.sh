TARGET_FILENAME="schattauer_msc_lq.pdf"

ps2pdf -dPDFSETTINGS=/ebook output/99-total.pdf "$TARGET_FILENAME"

MPQ_RZG_PATH="/home/max/Schattauer/DataShare"
HOME_RZG_PATH="/home/maxi/Masterarbeit"
if [ -d "$MPQ_RZG_PATH" ]
then
	cp "$TARGET_FILENAME" "$MPQ_RZG_PATH"
	echo "Copied to $MPQ_RZG_PATH" >&2
fi
if [ -d "$HOME_RZG_PATH" ]
then
	cp "$TARGET_FILENAME" "$HOME_RZG_PATH"
	echo "Copied to $HOME_RZG_PATH" >&2
fi
