# ZDI-23-1028: (Pwn2Own) Triangle MicroWorks SCADA Data Gateway Event Log Directory Traversal Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1028
- **ZDI-CAN:** ZDI-CAN-20534
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39460
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1028/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Triangle MicroWorks SCADA Data Gateway. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the creation of event logs. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
