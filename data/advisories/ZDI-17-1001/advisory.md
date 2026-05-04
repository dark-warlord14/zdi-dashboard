# ZDI-17-1001: WECON LeviStudio PLC Driver Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-1001
- **ZDI-CAN:** ZDI-CAN-5085
- **Date:** 2017-12-20
- **CVE:** CVE-2017-16717
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Wecon
- **Affected Products:** LeviStudio
- **Credit:** Michael DePlante
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-1001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of WECON LeviStudio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the handling of LeviStudio Project files. When parsing the Driver field, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Wecon has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-353-05

## Disclosure Timeline

- 2017-08-11 - Vulnerability reported to vendor
- 2017-12-20 - Coordinated public release of advisory
