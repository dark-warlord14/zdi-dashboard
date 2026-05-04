# ZDI-20-1068: (0Day) WECON LeviStudioU WordAlarmSet WordAddr9 Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1068
- **ZDI-CAN:** ZDI-CAN-10547
- **Date:** 2020-08-19
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** LeviStudioU
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1068/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WECON LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the WordAlarmSet tag within UMP files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/24/20 – ZDI reported the vulnerability to ICS-CERT 03/24/20 – ICS-CERT acknowledged the report 07/07/20 – ZDI requested an update 07/21/20 – ZDI requested an update 07/21/20 – ICS-CERT indicated there had been no reply from the vendor 07/31/20 – ZDI requested an update 08/13/20 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 08/18/20 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-03-24 - Vulnerability reported to vendor
- 2020-08-19 - Coordinated public release of advisory
