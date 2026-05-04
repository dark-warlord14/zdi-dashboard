# ZDI-21-588: Omron CX-One CX-Position NCI File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-588
- **ZDI-CAN:** ZDI-CAN-11845
- **Date:** 2021-05-13
- **CVE:** CVE-2021-27413
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-One
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-588/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Omron CX-One. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of NCI files in the CX-Position application. When parsing the B_PLC_NAME element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-131-01

## Disclosure Timeline

- 2021-01-20 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
