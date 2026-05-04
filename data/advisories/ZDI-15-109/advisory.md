# ZDI-15-109: (Pwn2Own) Mozilla Firefox Bounds Check Elimination Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-109
- **ZDI-CAN:** ZDI-CAN-2830
- **Date:** 2015-04-03
- **CVE:** CVE-2015-0817
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** i1xu1a
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-109/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of heap access bounds checking. A specially crafted typed array can eliminate bounds checks for heap accesses. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.mozilla.org/show_bug.cgi?id=1145255

## Disclosure Timeline

- 2015-03-19 - Vulnerability reported to vendor
- 2015-04-03 - Coordinated public release of advisory
