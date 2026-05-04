# ZDI-16-418: Adobe Reader DC choose XSLT Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-418
- **ZDI-CAN:** ZDI-CAN-3736
- **Date:** 2016-07-12
- **CVE:** CVE-2016-4195
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-418/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XPath expressions. A PDF document with a specific "choose" element and an XPath expression can force Adobe Reader DC to write values past the end of an allocated object. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-26.html

## Disclosure Timeline

- 2016-04-28 - Vulnerability reported to vendor
- 2016-07-12 - Coordinated public release of advisory
