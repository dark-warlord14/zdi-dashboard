# ZDI-16-477: PCRE Regular Expression Compilation Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-477
- **ZDI-CAN:** ZDI-CAN-3542
- **Date:** 2016-08-17
- **CVE:** CVE-2016-3191
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** PCRE
- **Affected Products:** PCRE
- **Credit:** Wei Lei Peng Haoxiang and Liu Yang of Nanyang Technological University
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-477/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of PCRE. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the compilation of regular expressions. The issue lies in the failure to validate that compilation of sub-groups will occur within the bounds of a fixed-size stack buffer. An attacker can leverage this vulnerability to execute code within the context of the current process.

## Additional Details

PCRE has issued an update to correct this vulnerability. More details can be found at: https://bugs.exim.org/show_bug.cgi?id=1791

## Disclosure Timeline

- 2016-02-09 - Vulnerability reported to vendor
- 2016-08-17 - Coordinated public release of advisory
