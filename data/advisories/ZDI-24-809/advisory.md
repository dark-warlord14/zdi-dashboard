# ZDI-24-809: (0Day) Actiontec WCB6200Q uh_get_postdata_withupload Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-809
- **ZDI-CAN:** ZDI-CAN-21418
- **Date:** 2024-06-18
- **CVE:** CVE-2024-6146
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Actiontec
- **Affected Products:** WCB6200Q
- **Credit:** Logan Stratton
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-809/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Actiontec WCB6200Q routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HTTP server. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the HTTP server.

## Additional Details

08/03/23 – ZDI requested vendor PSIRT contact. 08/11/23 – ZDI asked for an update. 09/18/23 – ZDI asked for an update. 09/18/23 – The vendor sent an automated support ticket response. 10/20/23 – ZDI asked for an update. 02/27/24 – ZDI sent the report to Actiontec support. 03/27/24 – The vendor sent an automated support ticket response. 06/17/27 – The ZDI informed the vendor that since we’ve never received a formal response to the report, that we intend to publish the report as a zero-day advisory on 6/18/24. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2024-02-27 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
