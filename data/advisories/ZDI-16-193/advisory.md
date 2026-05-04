# ZDI-16-193: Adobe Flash setInterval Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-193
- **ZDI-CAN:** ZDI-CAN-3546
- **Date:** 2016-03-10
- **CVE:** CVE-2016-0996
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** fujibayashi kyo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-193/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the setInterval method. By calling setInterval with specific arguments, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-08.html

## Disclosure Timeline

- 2016-02-02 - Vulnerability reported to vendor
- 2016-03-10 - Coordinated public release of advisory
