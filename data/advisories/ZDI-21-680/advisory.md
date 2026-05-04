# ZDI-21-680: (0Day) D-Link DAP-1330 lighttpd get_soap_action Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-680
- **ZDI-CAN:** ZDI-CAN-12066
- **Date:** 2021-06-10
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1330
- **Credit:** chung96vn of Vietnam National Cyber Security Center (NCSC Vietnam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-680/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-1330 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the SOAPAction HTTP header. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/29/21 – ZDI reported the vulnerabilities to the vendor 01/29/21 – The vendor acknowledged the report 05/20/21 – ZDI requested an update 05/23/21 – The vendor indicated they would provide an update in during the week 06/01/21 – ZDI requested an update and notified the vendor of the intention to publish the report as a 0-day advisory on 06/09/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-01-29 - Vulnerability reported to vendor
- 2021-06-10 - Coordinated public release of advisory
