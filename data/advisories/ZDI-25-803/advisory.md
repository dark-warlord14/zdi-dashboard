# ZDI-25-803: (0Day) (Pwn2Own) Kenwood DMX958XR libSystemLib Command injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-803
- **ZDI-CAN:** ZDI-CAN-26314
- **Date:** 2025-08-05
- **CVE:** CVE-2025-8655
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Kenwood
- **Affected Products:** DMX958XR
- **Credit:** Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-803/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Kenwood DMX958XR devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the firmware update process. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

01/23/25 – ZDI reported the vulnerability to the vendor. 01/23/25 – The vendor acknowledged the report. 05/15/25 – The vendor requested additional time to decide on whether a fix would be released. 05/16/25 – ZDI agreed to wait until May 30th. 06/25/25 – The vendor states that are working on the reported vulnerabilities 07/29/25 – ZDI asked for an update and informed the vendor that if there is not a patch available that we will publish the case as a zero-day advisory on 08/01/25. 07/31/25 – The vendor requested an extension till late September, to which ZDI declined. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-01-27 - Vulnerability reported to vendor
- 2025-08-05 - Coordinated public release of advisory
- 2025-08-05 - Advisory Updated
