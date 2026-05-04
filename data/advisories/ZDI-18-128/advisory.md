# ZDI-18-128: Wecon LeviStudioU General WriteAddr Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-128
- **ZDI-CAN:** ZDI-CAN-5311
- **Date:** 2018-01-18
- **CVE:** CVE-2017-16739
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Wecon
- **Affected Products:** LeviStudioU
- **Credit:** Sergey Zelenyuk of RVRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-128/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of WECON LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the handling of LeviStudioU Project files. When providing an overly long General WriteAddr XML attribute, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Wecon has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-011-01

## Disclosure Timeline

- 2017-12-01 - Vulnerability reported to vendor
- 2018-01-18 - Coordinated public release of advisory
