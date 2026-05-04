# ZDI-18-1109: (0Day) Wecon PIStudio basedll TextContent Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1109
- **ZDI-CAN:** ZDI-CAN-6253
- **Date:** 2018-10-02
- **CVE:** CVE-2018-14818
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Wecon
- **Affected Products:** PIStudio
- **Credit:** Natnael Samson(Natti)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1109/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wecon PIStudio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of hsc files. When parsing the TextContent element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of an administrator.

## Additional Details

Wecon has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/ICSA-18-277-01 This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/18/18 - ZDI sent the report to ICS-CERT 05/22/18 - ICS-CERT acknowledged, confirmed the report was sent to the vendor and sent an ICS-VU # 09/17/18 - ZDI asked ICS-CERT to confirm the report remains unpatched and to advise the vendor of the intent to publish the report as 0-day on 10/02/18 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-05-18 - Vulnerability reported to vendor
- 2018-10-02 - Coordinated public release of advisory
- 2021-12-02 - Advisory Updated
