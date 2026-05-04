# ZDI-21-778: (0Day) Advantech WebAccess Node BwImgExe Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-778
- **ZDI-CAN:** ZDI-CAN-13038
- **Date:** 2021-07-05
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-778/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within BwImgExe.exe, which is accessed through the 0x2711 IOCTL in the webvrpcs process. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/12/21 – ZDI reported the vulnerability to ICS-CERT 06/16/21 – ZDI requested an update 06/16/21 – ICS-CERT indicated that the vendor is still working on a fix 06/17/21 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 06/29/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-02-12 - Vulnerability reported to vendor
- 2021-07-05 - Coordinated public release of advisory
- 2021-07-07 - Advisory Updated
