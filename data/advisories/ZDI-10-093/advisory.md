# ZDI-10-093: Apple Webkit CSS Charset Text Transformation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-093
- **ZDI-CAN:** ZDI-CAN-765
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1770
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-093/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Webkit's support of character sets. If the IBM1147 character set is applied to a particular element and that element has a text transformation applied to it, the application will attempt to access an object that doesn't exist in order to perform the transformation. Successful exploitation will lead to code execution under the context of the web-browser.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-05-03 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
