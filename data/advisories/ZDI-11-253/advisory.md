# ZDI-11-253: Adobe Flash Player BitmapData.scroll Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-253
- **ZDI-CAN:** ZDI-CAN-1230
- **Date:** 2011-08-12
- **CVE:** CVE-2011-2138
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-253/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for evaluating the scroll method of the Actionscript Bitmap class. The function that uses the parameters to the scroll method performs arithmetic using data from the instantiated Bitmap object. By creating a Bitmap with certain integer values and subsequently calling the scroll method with other large integer values it is possible to force an integer wrap to occur. The resulting value is utilized to calculate a pointer which is operated upon by memory copy operations. By crafting specific values this issue can be exploited to execute remote code in the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-21.html

## Disclosure Timeline

- 2011-06-02 - Vulnerability reported to vendor
- 2011-08-12 - Coordinated public release of advisory
