# ZDI-16-220: Foxit Reader Revision Number Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-220
- **ZDI-CAN:** ZDI-CAN-3551
- **Date:** 2016-03-23
- **CVE:** CVE-2016-4063
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Mario Gomes(@NetFuzzer)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-220/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the object's revision number. A specially crafted object with a specific revision number in a PDF file can force a dangling pointer to be reused after it has been freed. An attacker could leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php Resolved with Foxit Reader 7.3.4

## Disclosure Timeline

- 2016-02-16 - Vulnerability reported to vendor
- 2016-03-23 - Coordinated public release of advisory
