# ZDI-22-345: (0Day) WECON LeviStudioU UMP File Parsing XY Tag WordAddr10 Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-345
- **ZDI-CAN:** ZDI-CAN-14408
- **Date:** 2022-02-15
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** LeviStudioU
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-345/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WECON LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XY tags within UMP files. When parsing the WordAddr10 attribute, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/05/21– ZDI reported the vulnerability to ICS-CERT 01/10/22 – ZDI requested an update 01/18/22 – ICS-CERT indicated that the vendor has not provided the fix 01/20/22 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 02/15/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-08-05 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
- 2022-02-17 - Advisory Updated
