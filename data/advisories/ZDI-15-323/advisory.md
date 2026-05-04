# ZDI-15-323: Adobe Reader ComboBox field Format action Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-323
- **ZDI-CAN:** ZDI-CAN-2757
- **Date:** 2015-07-14
- **CVE:** CVE-2015-5113
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-323/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the ComboBox fields with Format field actions. A specially crafted Text field with a Format field action can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-02-10 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
