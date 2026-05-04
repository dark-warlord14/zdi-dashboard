# ZDI-22-1458: GNU Gzip zgrep Argument Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1458
- **ZDI-CAN:** ZDI-CAN-16588
- **Date:** 2022-10-21
- **CVE:** N/A
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GNU
- **Affected Products:** Gzip
- **Credit:** cleemy desu wayo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1458/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GNU Gzip. Interaction with this script is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the handling of special characters. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system command. An attacker can leverage this vulnerability to execute code on the system.

## Additional Details

GNU has issued an update to correct this vulnerability. More details can be found at: https://lists.gnu.org/r/bug-gzip/2022-04/msg00011.html

## Disclosure Timeline

- 2022-03-23 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
