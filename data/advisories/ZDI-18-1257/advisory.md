# ZDI-18-1257: Laquis SCADA aq Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1257
- **ZDI-CAN:** ZDI-CAN-6544
- **Date:** 2018-10-16
- **CVE:** CVE-2018-17911
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** LAquis
- **Affected Products:** SCADA
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1257/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of LAquis SCADA. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within aq.exe. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this functionality to execute code in the context of the current process.

## Additional Details

LAquis has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-289-01

## Disclosure Timeline

- 2018-06-29 - Vulnerability reported to vendor
- 2018-10-16 - Coordinated public release of advisory
