# ZDI-16-273: Adobe Reader DC Graphics State Dictionary Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-273
- **ZDI-CAN:** ZDI-CAN-3431
- **Date:** 2016-04-28
- **CVE:** CVE-2016-1111
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-273/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Graphics State Dictionary parsing. A specially crafted Graphics State Dictionary inside a PDF document can trigger a double free condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-02.html

## Disclosure Timeline

- 2015-12-01 - Vulnerability reported to vendor
- 2016-04-28 - Coordinated public release of advisory
