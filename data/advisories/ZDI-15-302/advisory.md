# ZDI-15-302: (Pwn2Own) Adobe Reader array_push_slowly Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-302
- **ZDI-CAN:** ZDI-CAN-2823
- **Date:** 2015-07-14
- **CVE:** CVE-2015-5108
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** k33nteam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-302/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the array_push_slowly function. By specifying an invalid length, an integer overflow can occur resulting in an undersized buffer being allocated. A remote attacker could exploit this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
