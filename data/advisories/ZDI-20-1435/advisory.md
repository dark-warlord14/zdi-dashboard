# ZDI-20-1435: (0Day) D-Link DCS-960L HNAP Cookie Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1435
- **ZDI-CAN:** ZDI-CAN-11360
- **Date:** 2020-12-15
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DCS-960L
- **Credit:** phieulang aka Hoang Le of VietSunShine Cyber Security Services
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1435/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DCS-960L Wi-Fi cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the Cookie request header. The issue results from the lack of proper validation of a user-supplied string before using it as a format specifier. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/20/20 - ZDI reported the vulnerability to D-Link 10/16/20 - ZDI requested a status update 12/09/20 - ZDI notified D-Link of the intention to publish the report as 0-day advisory on 12/15/2020 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-07-20 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
- 2021-09-27 - Advisory Updated
