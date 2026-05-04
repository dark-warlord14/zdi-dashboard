# ZDI-23-1058: (0Day) (Pwn2Own) Softing edgeAggregator Restore Configuration Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1058
- **ZDI-CAN:** ZDI-CAN-20543
- **Date:** 2023-08-09
- **CVE:** CVE-2023-38126
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Softing
- **Affected Products:** edgeAggregator
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1058/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Softing edgeAggregator. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of backup zip files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this to execute code in the context of root.

## Additional Details

02/15/23 – The ZDI reported this vulnerability to the vendor during the Pwn2Own Miami contest. 02/20/23 – The vendor states they would review and report back with the security advisories. 03/08/23 – The vendor requested CVE Numbers. 03/15/23 – ZDI provided the vendor with CVE numbers. 07/31/23 – ZDI asked for an update. 08/03/23 – ZDI asked for an update. 08/07/23 – The ZDI asked for an update and informed the vendor that we are publishing this case as a zero-day advisory on 08/09/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-02-23 - Vulnerability reported to vendor
- 2023-08-09 - Coordinated public release of advisory
