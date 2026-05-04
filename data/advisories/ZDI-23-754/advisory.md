# ZDI-23-754: (0Day) Microsoft 3D Viewer FBX File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-754
- **ZDI-CAN:** ZDI-CAN-18521
- **Date:** 2023-05-31
- **CVE:** CVE-2023-27911
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** 3D Viewer
- **Credit:** Mat Powell & Michael DePlante (@izobashi) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-754/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft 3D Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FBX files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

08/25/22 – ZDI reported the vulnerability to the vendor. 08/31/22 – The vendor acknowledged the report. 09/09/22 – The vendor confirmed the vulnerability. 03/10/23 – ZDI informed the vendor that this case will be published as a zero-day advisory on 03/14/23. 03/13/23 – The vendor informed the ZDI that they patched numerous cases that were scheduled to be published as zero-day advisories. 05/24/23 – The vendor categorized this case as low severity, and the ZDI rescheduled the publication date to 05/31/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application. Microsoft published a public advisory on September 12, 2023. https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-27911

## Disclosure Timeline

- 2022-08-25 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
- 2023-09-12 - Advisory Updated
