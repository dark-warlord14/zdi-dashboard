# ZDI-20-1438: (0Day) D-Link DCS-960L HTTP Authorization Header Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1438
- **ZDI-CAN:** ZDI-CAN-11359
- **Date:** 2020-12-15
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DCS-960L
- **Credit:** chung96vn of Vietnam's NCSC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1438/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DCS-960L Wi-Fi cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HTTP server, which listens on TCP port 80 by default. A crafted Authorization header in an HTTP request can trigger an overflow of a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/09/20 - ZDI reported the vulnerability to D-Link 10/16/20 - ZDI requested a status update 12/09/20 - ZDI notified D-Link of the intention to publish the report as 0-day advisory on 12/15/2020 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-07-29 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
