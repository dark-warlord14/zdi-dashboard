# ZDI-18-406: Wecon LeviStudioU DataLogTool INI Parser Stack-based Buffer Overflow Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-406
- **ZDI-CAN:** ZDI-CAN-5480
- **Date:** 2018-05-04
- **CVE:** CVE-2018-7527
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Wecon
- **Affected Products:** LeviStudioU
- **Credit:** Sergey Zelenyuk of RVRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-406/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Wecon LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within DataLogTool.exe. When parsing a string within an INI file, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Wecon has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-116-02

## Disclosure Timeline

- 2017-12-21 - Vulnerability reported to vendor
- 2018-05-04 - Coordinated public release of advisory
- 2018-05-04 - Advisory Updated
