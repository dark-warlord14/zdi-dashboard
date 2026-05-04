# ZDI-13-003: Mozilla Firefox String Replacement Heap Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-003
- **ZDI-CAN:** ZDI-CAN-1473
- **Date:** 2013-02-01
- **CVE:** CVE-2013-0750
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** pa_kt / twitter.com/pa_kt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-003/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Mozilla Firefox handles the concatenation of strings. By causing concatenation of specially crafted strings, an integer overflow may occur resulting in an undersized allocation. Subsequent use of this undersized memory allocation results in memory corruption, which may be exploited by an attacker to gain remote code execution.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2013/mfsa2013-12.html

## Disclosure Timeline

- 2012-10-24 - Vulnerability reported to vendor
- 2013-02-01 - Coordinated public release of advisory
