# ZDI-17-316: Hewlett Packard Enterprise Intelligent Management Center imcwlandm UserName Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-316
- **ZDI-CAN:** ZDI-CAN-4539
- **Date:** 2017-05-03
- **CVE:** CVE-2017-5805
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Intelligent Management Center
- **Credit:** sztivi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-316/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HPE iMC Server service, which listens on UDP port 6666 by default. When parsing the UserName attribute, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20564.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbhf03738en_us

## Disclosure Timeline

- 2017-03-01 - Vulnerability reported to vendor
- 2017-05-03 - Coordinated public release of advisory
