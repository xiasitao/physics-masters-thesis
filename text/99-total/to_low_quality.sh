ps2pdf -dPDFSETTINGS=/ebook output/99-total.pdf lq.pdf

MPQ_RZG_PATH="/home/max/Schattauer/DataShare"
HOME_RZG_PATH="/home/maxi/Masterarbeit"
if [ -d "$MPQ_RZG_PATH" ]
then
	cp lq.pdf "$MPQ_RZG_PATH"
	echo "Copied to $MPQ_RZG_PATH" >&2
fi
if [ -d "$HOME_RZG_PATH" ]
then
	cp lq.pdf "$HOME_RZG_PATH"
	echo "Copied to $HOME_RZG_PATH" >&2
fi
