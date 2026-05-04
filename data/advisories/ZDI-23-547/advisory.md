# ZDI-23-547: (0Day) Linux Kernel IPv6 RPL Protocol Reachable Assertion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-547
- **ZDI-CAN:** ZDI-CAN-16223
- **Date:** 2023-05-04
- **CVE:** CVE-2023-2156
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** maxpl0it (@maxpl0it)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-547/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the RPL protocol. The issue results from the lack of proper handling of user-supplied data, which can result in an assertion failure. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

01/26/22 – ZDI reported the vulnerability to the vendor. 02/02/22 – The vendor acknowledged the report. 08/24/22 – ZDI asked for an update. 08/24/22 – The vendor asked for additional details about the vulnerability. 09/19/22 – The vendor states that there is a patch, but the ZDI informed the vendor that the bug is still triggerable on the latest mainline. 10/05/22 – ZDI provided additional details. 10/07/22 – The vendor states there is a new patch, but the ZDI was able to reproduce the vulnerability on the latest mainline. 10/26/22 – The vendor informed the ZDI that they would continue to investigate. 04/12/23 – ZDI asked for an update. 04/14/23 – The vendor informed the ZDI that a new patch would merge into the latest mainline on 04/21/2023. 04/21/23 – The original finder reports to the vendor that the patch may not work, and it was confirmed by the ZDI that the vulnerability is reproducible on the latest mainline. 05/02/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 05/04/23, and in coordination with Red Hat this vulnerability will be assigned CVE-2023-2156. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory
