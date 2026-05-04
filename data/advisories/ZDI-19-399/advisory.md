# ZDI-19-399: Delta Industrial Automation CNCSoft ScreenEditor DPB File Parsing wTextLen Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-399
- **ZDI-CAN:** ZDI-CAN-7807
- **Date:** 2019-04-17
- **CVE:** CVE-2019-10947
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Industrial Automation
- **Affected Products:** CNCSoft ScreenEditor
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-399/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Delta Industrial Automation CNCSoft ScreenEditor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DPB files. When parsing the wTextLen element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the Administrator.

## Additional Details

Delta Industrial Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-106-01

## Disclosure Timeline

- 2019-01-11 - Vulnerability reported to vendor
- 2019-04-17 - Coordinated public release of advisory
