# ZDI-24-1048: (0Day) (Pwn2Own) ChargePoint Home Flex onboardee Improper Access Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1048
- **ZDI-CAN:** ZDI-CAN-23150
- **Date:** 2024-08-01
- **CVE:** CVE-2024-23920
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ChargePoint
- **Affected Products:** Home Flex
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1048/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of ChargePoint Home Flex charging stations. Authentication is not required to exploit this vulnerability. The specific flaw exists within the onboardee module. The issue results from improper access control. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

01/28/24 – ZDI reported the vulnerability to the vendor. 02/05/24 – ZDI asked for confirmation of receipt. 02/06/24 – The vendor confirmed receipt of the report. 04/29/24 – ZDI asked for an update. 05/24/24 – ZDI asked for an update. 05/29/24 – The vendor states that the vulnerability has been addressed but would need to get verification from QA. 07/22/24 – ZDI asked for an update. 07/29/24 – The ZDI informed the vendor that since we never received a confirmation that the vulnerability was patched, we have no choice but to assume this issue hasn’t been remediated and that we intend to publish the report as a zero-day advisory on 8/01/24. --Vendor Response 08/16/24: The vendor states this vulnerability was patched in May 2024.

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-08-01 - Coordinated public release of advisory
- 2024-08-21 - Advisory Updated
