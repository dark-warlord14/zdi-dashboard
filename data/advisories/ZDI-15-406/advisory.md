# ZDI-15-406: Mozilla Firefox nsIPresShell Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-406
- **ZDI-CAN:** ZDI-CAN-2938
- **Date:** 2015-08-31
- **CVE:** CVE-2015-4497
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Ucha Gobejishvili
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-406/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of nsIPresShell. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2015-94/

## Disclosure Timeline

- 2015-06-16 - Vulnerability reported to vendor
- 2015-08-31 - Coordinated public release of advisory
