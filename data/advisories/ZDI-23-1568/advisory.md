# ZDI-23-1568: NI Measurement & Automation Explorer Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1568
- **ZDI-CAN:** ZDI-CAN-21354
- **Date:** 2023-10-19
- **CVE:** CVE-2023-4601
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** Measurement & Automation Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1568/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NI Measurement & Automation Explorer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of response data from devices. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/documentation/supplemental/23/stack-based-buffer-overflow-in-ni-system-configuration.html

## Disclosure Timeline

- 2023-07-07 - Vulnerability reported to vendor
- 2023-10-19 - Coordinated public release of advisory
