# ZDI-15-215: Adobe Acrobat Pro Close page action Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-215
- **ZDI-CAN:** ZDI-CAN-2724
- **Date:** 2015-05-12
- **CVE:** CVE-2015-3053
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-215/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Close page action. A specially crafted Close page action can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Disclosure Timeline

- 2015-02-04 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
