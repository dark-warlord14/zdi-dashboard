# ZDI-14-323: Adobe Reader replace() Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-323
- **ZDI-CAN:** ZDI-CAN-2432
- **Date:** 2014-09-16
- **CVE:** CVE-2014-0567
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-323/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the replace() JavaScript function. By creating a specially crafted string followed by a replace call with specific arguments, an attacker can force a heap buffer to overflow. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://t.info.adobesystems.com//r/?id=t35c7e2bc,808fe4f,83a379a

## Disclosure Timeline

- 2014-07-24 - Vulnerability reported to vendor
- 2014-09-16 - Coordinated public release of advisory
