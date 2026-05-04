# ZDI-21-155: (0Day) D-Link DAP-3662 httpd Authentication Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-155
- **ZDI-CAN:** ZDI-CAN-11206
- **Date:** 2021-02-09
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-3662
- **Credit:** chung96vn of Vietnam's NCSC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-155/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DAP-3662 Wi-Fi access points. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the httpd web server. A crafted HTTP request can bypass the authentication mechanism. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/19/20 – ZDI reported the vulnerability to the vendor 01/08/21 – ZDI requested an update 01/11/21 – The vendor indicated the case would be published during the week 01/18/21 – ZDI requested an update 01/18/21 – The vendor indicated they would have a resolution during the week 01/24/21 – The vendor indicated they expected to close the issue during the week 02/01/21 – ZDI requested and update and notified the vendor of the intention to publish the report as 0-day advisory on 02/09/21 02/01/21 – The vendor acknowledged and indicated they would work on the fix -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-08-19 - Vulnerability reported to vendor
- 2021-02-09 - Coordinated public release of advisory
