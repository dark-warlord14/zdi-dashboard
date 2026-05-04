# ZDI-16-215: Foxit Reader XFA remerge Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-215
- **ZDI-CAN:** ZDI-CAN-3521
- **Date:** 2016-03-23
- **CVE:** CVE-2016-4064
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-215/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XFA forms. A specially crafted remerge call can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php Resolved with Foxit Reader 7.3.4

## Disclosure Timeline

- 2016-02-02 - Vulnerability reported to vendor
- 2016-03-23 - Coordinated public release of advisory
