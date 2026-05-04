# ZDI-15-036: Motorola Scanner SDK rsmdriverproviderservice.exe Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-036
- **ZDI-CAN:** ZDI-CAN-2516
- **Date:** 2015-02-10
- **CVE:** CVE-2015-1496
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Motorola
- **Affected Products:** Scanner SDK
- **Credit:** kernelsmith - Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-036/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code with elevated privileges on vulnerable installations of Motorola Scanner SDK. Authentication is not required to exploit this vulnerability. The specific flaw exists within the file permissions (ACLs) on an installed directory. RSMDriverProviderService.exe is vulnerable to tampering by all users. A local attacker can leverage this vulnerability to raise privileges and execute code under the context of SYSTEM.

## Additional Details

Motorola has issued an update to correct this vulnerability. More details can be found at: https://portal.motorolasolutions.com/Support/US-EN/Resolution?solutionId=87666&redirectForm=search&searchQuery=%3FsearchType%3Dsimple%26searchTerm%3Dscanner%20sdk

## Disclosure Timeline

- 2014-09-05 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
