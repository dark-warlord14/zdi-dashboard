# ZDI-22-142: WECON LeviStudioU UMP File Parsing Trend Tag WordAddr Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-142
- **ZDI-CAN:** ZDI-CAN-14722
- **Date:** 2022-01-27
- **CVE:** CVE-2021-23138
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** LeviStudioU
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-142/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WECON LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of Trend tags within UMP files. When parsing the WordAddr attribute, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

WECON has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-21-355-03

## Disclosure Timeline

- 2021-08-20 - Vulnerability reported to vendor
- 2022-01-27 - Coordinated public release of advisory
