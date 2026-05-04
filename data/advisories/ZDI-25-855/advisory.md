# ZDI-25-855: Cockroach Labs cockroach-k8s-request-cert Empty Root Password Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-855
- **ZDI-CAN:** ZDI-CAN-22195
- **Date:** 2025-08-27
- **CVE:** CVE-2025-9276
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cockroach Labs
- **Affected Products:** cockroach-k8s-request-cert
- **Credit:** Alfredo de Oliveira - Trend Micro Nebula Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-855/
## Vulnerability Details

This vulnerability could allow remote attackers to bypass authentication on systems that use the affected version of the Cockroach Labs cockroach-k8s-request-cert container image. The specific flaw exists within the configuration of the system shadow file. The issue results from a blank password setting for the root user. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

10/06/2023 – ZDI attempted to contact the vendor multiple times, but no response was received 08/08/2025 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Update 08/27/2025 ZDI acknowledges that the contact requests were not submitted through Cockroach Labs’ official vulnerability disclosure designated channel. As a result, the vendor was not aware of the issue. However, messages sent through other vendor’s official contacts over the past two years went unanswered. Cockroach Labs received the report on 08/25/2025 and confirmed that the container image is no longer a component of Cockroach Labs' supported service. Both parties remain committed to the users’ protection

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-08-27 - Coordinated public release of advisory
- 2025-08-27 - Advisory Updated
