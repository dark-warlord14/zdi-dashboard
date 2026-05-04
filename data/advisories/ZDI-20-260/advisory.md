# ZDI-20-260: (0Day) AMD Radeon Divide By Zero Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-260
- **ZDI-CAN:** ZDI-CAN-8315
- **Date:** 2020-02-20
- **CVE:** N/A
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** AMD
- **Affected Products:** Radeon
- **Credit:** Lilang Wu and Moony Li of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-260/
## Vulnerability Details

This vulnerability allows local attackers to trigger a Denial-of-Service condition on vulnerable installations of AMD Radeon drivers on Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AMD Radeon driver. 3D rendering under certain conditions can trigger an unhandled exception. An attacker can leverage this vulnerability to deny access to the target system.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/09/19 – ZDI sent the vulnerability report to the vendor 12/27/19 - ZDI requested any available update 12/29/19 - The vendor replied that "we do not have a record of this message reaching the AMD PSIRT team previously," but that they would review the report, and “will let you know of our findings” 12/30/19 - ZDI replied that "this report was sent on Tuesday 07/09/19" and asked the vendor to please look 01/14/20 - ZDI requested any available update 01/29/20 - ZDI requested any available update 02/05/20 - ZDI requested any available update and advised the vendor of the intent to publish this report as a 0-day advisory on 02/20/20 due to the lack of response -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2019-07-09 - Vulnerability reported to vendor
- 2020-02-20 - Coordinated public release of advisory
