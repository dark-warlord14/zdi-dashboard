# ZDI-21-399: (0Day) D-Link DIR-882 HNAP Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-399
- **ZDI-CAN:** ZDI-CAN-11682
- **Date:** 2021-03-31
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-882
- **Credit:** phieulang aka Hoang Le of VietSunShine Cyber Security Services
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-399/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-882 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HNAP service, which listens on TCP port 80 by default. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/02/20 – ZDI reported the vulnerability to the vendor 02/03/21 – ZDI requested an update 03/23/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 03/30/21 03/29/21 - The vendor posted a vulnerability announcement https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10215 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-10-02 - Vulnerability reported to vendor
- 2021-03-31 - Coordinated public release of advisory
- 2021-09-27 - Advisory Updated
